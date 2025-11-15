# INFO:
- **This is a code, that goes through parties (Randomly for better results) and saves the results**

## SETUP:
- Always use alts.
### Tokens (Replace only if the code says "Wrong Tokens"):
1. Go to DevTools -> Network
2. Join a party
3. Find the request
4. Press "View Source"
5. Copy Payload
6. Paste it into the function gen_payload
7. Replace your party code with the variable partyCode, e.g. {"partyCode":"1XD"} -> {"partyCode":partyCode}
### Account Username (Variable: starterName):
- It will not call an error, but it will mark all parties as parties with people
<details>
  <summary>Show image</summary>
<img width="281" height="380" alt="image" src="https://github.com/user-attachments/assets/a2b666d1-9e2f-46af-96bb-519076545e8c" />
</details>

1. Go to bloxd
2. Remember the username
3. Replace "**Startername**" in code with the start of your name (no matter how many letters you are going to put in there, you can even put your whole name in it.)

### Bloxd API URL:
- Can change once in a while.
- You can notice it if the code says "Not found party..." for a very long time
1. Go to your request (See *Tokens*)
2. Go to Headers
3. Copy the URL header
<details>
  <summary>Show image</summary>
<img width="240" height="313" alt="image" src="https://github.com/user-attachments/assets/d04cbef9-2bc7-4ba9-b78e-b1affb60950f" />
</details>

### Modules (You may have them installed)
#### Cause "module not found" error
- colorama (For coloring text)
- requests (For making API requests)
<details>
  <summary>Show image</summary>
<img width="639" height="69" alt="image" src="https://github.com/user-attachments/assets/adc7eb0b-71bd-42a1-897d-abc3fdf4ee48" />
</details>

## Usage:
### Just run the script. It can log 4 types of messages, if the code is run correctly.
- Successfully joined *\*Party\**. - Party was joined successfully and its code was logged in ALLOWED.json
<details>
  <summary>Show image</summary>
<img width="323" height="37" alt="image" src="https://github.com/user-attachments/assets/5c32bb26-f804-4048-b04e-2dcc70324f99" />
</details>

- Party *\*Party\** not found. - Party unavailable
<details>
  <summary>Show image</summary>
<img width="214" height="48" alt="image" src="https://github.com/user-attachments/assets/69bdf3d4-8c2c-47eb-b503-cde6d30b6aaa" />
</details>

- Party *\*Party\** is not empty. - Party has people in it \[Somebody with different username as starterName is the leader of the party\] - Party code & Leader name are logged into BLOXD_PARSED_PARTIES.txt
<details>
  <summary>Show image</summary>
<img width="986" height="71" alt="image" src="https://github.com/user-attachments/assets/a8650bbf-3543-41f4-b13f-1f23822c8bd0" />
</details>

- STOPPED - You've stopped the code and the results are being saved...
<details>
  <summary>Show image</summary>
<img width="86" height="49" alt="image" src="https://github.com/user-attachments/assets/fd998960-f521-477c-b25b-f1e1cef7a893" />
</details>

# [Our Discord](https://discord.gg/x74tzmAdpA)
