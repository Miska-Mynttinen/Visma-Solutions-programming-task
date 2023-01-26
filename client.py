from identify_request import IdentifyRequest

# Client done as simple printing to terminal tests for the class
def main():
  # Test for basic login example
  request1 = IdentifyRequest("visma-identity://login?source=severa")
  values1 = request1.verify()
  print(values1[0])
  print(values1[1])

  # Test for basic confirm example
  request2 = IdentifyRequest("visma-identity://confirm?source=netvisor&paymentnumber=102226")
  values2 = request2.verify()
  print(values2[0])
  print(values2[1])

  # Test for basic sign example
  request3 = IdentifyRequest("visma-identity://sign?source=vismasign&documentid=105ab44")
  values3 = request3.verify()
  print(values3[0])
  print(values3[1])


  # Checking validation so they return error messages to the terminal

  # Test for URI validation
  request4 = IdentifyRequest(1)
  values4 = request4.verify()

  # Test for URI has enough components
  request5 = IdentifyRequest("visma-identity://login")
  values5 = request5.verify()

  # Test for scheme validation
  request6 = IdentifyRequest("visma-identi://login?source=severa")
  values6 = request6.verify()

  # Test for path validation
  request7 = IdentifyRequest("visma-identity://lofail?source=severa")
  values7 = request7.verify()

  # Test for login parameter source validation - kind of useless because the URI is a string
  request8 = IdentifyRequest("visma-identity://login?source=somestring")
  values8 = request8.verify()
  if type(values8[1]["source"]) is str:
    print("Source is a string")

  # Test for confirm parameter payment number validation
  request9 = IdentifyRequest("visma-identity://confirm?source=netvisor&paymentnumber=1022asd26")
  values9 = request9.verify()

  # Test for sign parameter documentid validation - kind of useless because the URI is a string
  request10 = IdentifyRequest("visma-identity://sign?source=vismasign&documentid=somestring")
  values10 = request10.verify()
  if type(values10[1]["documentid"]) is str:
    print("Documentid is a string")

main()