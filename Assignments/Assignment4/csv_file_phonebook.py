import csv
data=[["NAME","ADDRESS","MOBILE_NO","E_MAIL"],
      ["RAM","KANPUR","9199345261","ram@gmail.com"],
      ["SHYAM","MUMBAI","6567484646","shyam@gmail.com"],
      ["KARAN","JAIPUR","546463773I","karan@gmail.com"],
      ["JAY","JAIPUR","928739773I","jay@gmail.com"]]
with open("address_phonebook.csv","w",newline="") as file:
    writer=csv.writer(file)
    for x in data:
        writer.writerow(x)