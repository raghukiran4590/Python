on run argv
	set theAttachment to item 1 of argv
	set theAttachment to theAttachment as POSIX file --convert to posix file

	tell application "Microsoft Outlook"

	activate -- Opens and brings Outlook to the front
	
	--Set Current Date
	set shortDate to short date string of (current date)
	
	-- Create a new outgoing message
	set newMessage to make new outgoing message with properties {subject:"AWS Files " & shortDate & "", content:"Please find the attached AWS Files for " & shortDate & "."}
	
	-- Add recipients
	-- make new recipient at newMessage with properties {email address:{name:"Kiran, Raghu", address:"raghu.kiran@elevancehealth.com"}}
	make new recipient at newMessage with properties {email address:{name:"Pease, Daniel", address:"daniel.pease@elevancehealth.com"}}
	make new recipient at newMessage with properties {email address:{name:"Budreau, Chuck", address:"charles.budreau@elevancehealth.com"}}
	make new recipient at newMessage with properties {email address:{name:"Strange, James", address:"james.strange@elevancehealth.com"}}
	
	-- Optional: Add a CC or BCC recipient
	make new cc recipient at newMessage with properties {email address:{name:"dl-InfoHub-Support", address:"dl-infohub-support@anthem.com"}}
	-- make new bcc recipient at newMessage with properties {email address:{name:"BCC Recipient", address:"bcc@example.com"}}
	
	-- Optional: Add an attachment
	tell newMessage --tell theMessage (not theContent) to add the attachment
            make new attachment with properties {file:theAttachment}
    end tell
	--make new attachment at newMessage with properties {file:attachmentPath}

	-- Open the message for review (if not sending automatically)
	--open newMessage
	
	-- Send the message (uncomment the line below to send automatically)
	send newMessage
	
	end tell
end run