try:
    f = open('test_file.text','r')
except FileNotFoundError as fnf_error:
    print(fnf_error)
   
       
