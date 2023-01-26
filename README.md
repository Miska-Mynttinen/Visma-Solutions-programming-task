# Description
A simple Class for URI verification.
Client uses the class with simple tests that call the verify function of the class IdentifyRequest.
Created with Python.

## Running the program
Run the client.py file to see the the result in terminal.

### I understood the problem as a simple class that needed to check a lot of things were right and return values based on given URI.
Verify function of the class IdentifyRequest handles the whole problem due to it being simple and not needing extra parts.
I put the parser and checkParameters functions inside the verify function, because they serve no function other than to be used in the verify function and shouldn't be accessed any other way.

### Challenges were bloating of a functions due to parsing of the parameters and checking all of the validators.
The parsing of the parameters repeated a lot of code because login was different from confirm and sign. This caused a lot of repeated code in places that should be cleaned.

Validators take up a lot of code for simple things and don't look very clean.


## The given problem
### Your task is to design and implement a class which is responsible for identifying what kind of requests it receives. Other apps can call the identity app using the scheme visma-identity.
A uri consists of three parts:
Example: visma-identity://login?source=severa
Scheme: visma-identity
Path: login
Parameters: source=severa

The class needs to satisfy the following requirements:
1. It takes the following information as input
    URI (type: string)
    Example: visma-identity://login?source=severa
2. It has to parse and validate that:
    Used URI scheme is right: visma-identity
    Path is one of the allowed: login, confirm or sign
3. All parameters for a path are valid
4. Requirements for the parameters:
      - Path login:
      source(type:string)
      Example: visma-identity://login?source=severa
      - Path confirm:
      source(type:string)
      payment number(type:integer)
      Example: visma-identity://confirm?source=netvisor&paymentnumber=102226
      - Path sign:
     source(type: string)
     documentid(type:string)
     Example: visma-identity://sign?source=vismasign&documentid=105ab44
5. Class returns:
     Path
     Parameters as key value pairs
6. Is designed using the practises of object-oriented programming
7. Implementation needs to have a client, which uses the new class. You can for example implement the client as another class that uses the relevant methods.

Write a short description of how you understood the problem, what challenges you had with the implementation and what you could further improve in your implementation. If you had to make compromises, we would like to hear about them.

Use about two to three hours for this task, including writing the description.
