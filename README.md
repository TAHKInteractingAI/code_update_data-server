# update_data_200gb_code
Code used to update data 200gb after decompression.
Instructions for using the linkedIn data update tool after extracting the 200GB Dataset from the server.

In the folder include:

![image](https://github.com/botsamqntdata/update_data_200gb_code/assets/128407982/f648a3a7-714f-4884-8870-3200ebec1275)

Step 1: Add an excel file containing linkedIn links that need to be updated

Step 2: replace the name “info” with the newly added file name

Adjust rows and columns containing linkedIn links that need updating

below is the 5th Column, lines 2 to 68

  df=pd.read_excel('info.xlsx') # Enter excel file name

  data_list=df.iloc[1:68,5].values.tolist()

Step 3: Enter the userName and password of a linkedIn account

  input_username.send_keys ("username")# enter username

  input_pass.send_keys("password")# enter password
  
  Step 4: Enter the name of the excel file to export after successful update
  
      data.to_excel('filename.xlsx',index=False)
      
 after success will get an excel file 'filename.xlsx' in the same folder
