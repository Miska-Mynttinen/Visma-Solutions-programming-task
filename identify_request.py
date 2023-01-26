class IdentifyRequest:

  def __init__(self, given_uri):
    # Initialises class for given parameter URI
    self.__uri = given_uri

  
  def verify(self):
    # helper function to parse URI into scheme, path and parameters
    def parser(uri):
      parsed1 = uri.split("://")
      parsed2 = parsed1[1].split("?")
      return (parsed1[0], parsed2[0], parsed2[1])

    # helper function to check parameters for the different path cases
    def checkParameters(parameters, path):
      match path:

        case "login":
          split_parameters = parameters.split("=")
          if type(split_parameters[1]) is not str:
            print("URI source is incorrect type, should be string")
            return 0

        case "confirm":
          split_parameters = parameters.split("&")
          split_parameters_left = split_parameters[0].split("=")
          split_parameters_right = split_parameters[1].split("=")
          split_parameters = split_parameters_left + split_parameters_right
          if type(split_parameters[1]) is not str:
            print("URI source is incorrect type, should be string")
            return 0
          try:
            split_parameters[2] = int(split_parameters[3])
          except ValueError:
            print("URI payment number is incorrect type or style, should be integer")
            return 0

        case "sign":
          split_parameters = parameters.split("&")
          split_parameters_left = split_parameters[0].split("=")
          split_parameters_right = split_parameters[1].split("=")
          split_parameters = split_parameters_left + split_parameters_right
          if type(split_parameters[1]) is not str:
            print("URI source is incorrect type, should be string")
            return 0
          elif type(split_parameters[3]) is not str:
            print("URI documentid is incorrect type, should be string")
            return 0

    # Check if given URI is not a string
    if type(self.__uri) is not str:
      print("Error URI is not a string")
      return

    # Parse URI and check if all components exist
    try:
      parsed_uri = parser(self.__uri)
      scheme = parsed_uri[0]
      path = parsed_uri[1]
      parameters = parsed_uri[2]
    except IndexError:
      print("URI has too little components")
      return

    # Validate shceme and path are correct
    if scheme != "visma-identity":
      print("URI shcheme is incorrect")
      return
    if not(path == "login" or path == "confirm" or path == "sign"):
      print("URI path is incorrect")
      return
    
    # Checking if given source parameter is correct for the path login, confirm or sign
    try:
      if checkParameters(parameters, path) == 0:
        return
    except IndexError:
      print("not enough parameters for path type")
      return

    # Split parameters and return path and parameters based on path
    if path == "login":
      parameters = parameters.split("=")
      return (path, {parameters[0]: parameters[1]})

    if path == "confirm":
      parameters = parameters.split("&")
      parameters_left = parameters[0].split("=")
      parameters_right = parameters[1].split("=")
      parameters = parameters_left + parameters_right
      return (path, {parameters[0]: parameters[1], parameters[2]: int(parameters[3])})

    if path == "sign":
      parameters = parameters.split("&")
      parameters_left = parameters[0].split("=")
      parameters_right = parameters[1].split("=")
      parameters = parameters_left + parameters_right
      return (path, {parameters[0]: parameters[1], parameters[2]: parameters[3]})