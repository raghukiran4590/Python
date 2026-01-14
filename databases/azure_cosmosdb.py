# pip install azure-cosmos
# pip install aiohttp

from azure.cosmos.aio import CosmosClient # pyright: ignore[reportMissingImports]
from azure.cosmos import exceptions # pyright: ignore[reportMissingImports]
from azure.cosmos.partition_key import PartitionKey # pyright: ignore[reportMissingImports]
import asyncio

# Replace these values with your Cosmos DB connection information
endpoint = "https://azure-cosmos-nosql.documents.azure.com:443/"
key = "master_key"
database_id = "cosmicwerx"
container_id = "cosmicontainer"
partition_key = "/partition_key"

# Set the total throughput (RU/s) for the database and container
database_throughput = 1000

# Singleton CosmosClient instance
client = CosmosClient(endpoint, credential=key)

# Helper function to get or create database and container
async def get_or_create_container(client, database_id, container_id, partition_key):
    database = await client.create_database_if_not_exists(id=database_id)
    print(f'Database "{database_id}" created or retrieved successfully.')

    container = await database.create_container_if_not_exists(id=container_id, partition_key=PartitionKey(path=partition_key))
    print(f'Container with id "{container_id}" created')
 
    return container
 
async def create_products():
    container = await get_or_create_container(client, database_id, container_id, partition_key)
    for i in range(10):
        await container.upsert_item({
            'id': f'item{i}',
            'productName': 'Widget',
            'productModel': f'Model {i}'
        })
 
async def get_products():
    items = []
    container = await get_or_create_container(client, database_id, container_id, partition_key)
    async for item in container.read_all_items():
        items.append(item)
    return items

async def query_products(product_name):
    container = await get_or_create_container(client, database_id, container_id, partition_key)
    query = f"SELECT * FROM c WHERE c.productName = '{product_name}'"
    items = []
    async for item in container.query_items(query=query, enable_cross_partition_query=True):
        items.append(item)
    return items

async def main():
    await create_products()
    all_products = await get_products()
    print('All Products:', all_products)

    queried_products = await query_products('Widget')
    print('Queried Products:', queried_products)

if __name__ == "__main__":
    asyncio.run(main())