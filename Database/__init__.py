import openpyxl
from Image_Detection import final_output

def give_path(path):
    import os
    paths=[]
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if (filename.endswith('.jpg') or filename.endswith('.jpeg')  or filename.endswith('.png')):
                paths.append(os.sep.join([dirpath, filename]))

    return(paths)

if __name__ == "__main__":
    image_paths = give_path("/Users/ashivalagar/Desktop/images")

    database_workbook = openpyxl.Workbook()
    database = database_workbook.active

    for i in range(len(image_paths)):
  
        curr_image_path = image_paths[i]

        curr_col1 = database["A"+str(i+2)]
        curr_col2 = database["B"+str(i+2)]
        curr_col3 = database["C"+str(i+2)]

        curr_output = final_output(curr_image_path)

        curr_col1.value = i+1
        curr_col2.value = curr_output['labels']
        curr_col3.value = curr_output['text']

        print("Count:",i+1)
        print("Image path:",curr_image_path)
        database_workbook.save('./database.xls')
