def count_errors(log_file):
   count = 0
   log_file = r"C:\Users\manib\PythonCoding\logs\app.log"
   with open(log_file, "r") as f:
      for line in f:
         if "ERROR" in line:
            count += 1
   return count
if __name__ == "__main__":
   print(count_errors("logs/app.log"))
