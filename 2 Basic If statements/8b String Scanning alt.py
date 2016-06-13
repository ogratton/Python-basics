while 1:
    line = input("Line: ")
    robots = False
    robot_pos = "No robots here."
    robot_right = False
    robot_left = False


    if "robot" in line.lower():
      robot_pos = line.lower().index("robot")
      
      if robot_pos == 0:
        robot_left = True
      if robot_pos > 0:
        if line[robot_pos - 1] in [" ", ",", ".", "?", ":", "'", '"']:
          robot_left = True
          
      if len(line) == robot_pos + 5:
        robot_right = True  
      if len(line) > robot_pos + 5:
        if line[robot_pos + 5] in [" ", ",", ".", "?", ":", "'", '"']:
          robot_right = True

    if robot_left and robot_right:
      robots = True

    if robots:
      if "robot" in line:
        print("There is a small robot in the line.")
        
      elif "ROBOT" in line:
        print("There is a big robot in the line.")
      
      else:
        print("There is a medium sized robot in the line.")
        
    else:
      print("No robots here.")
        

