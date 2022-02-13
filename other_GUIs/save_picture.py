from face_recognize import *

class Save_picture():
    def main(self, f_faces, user):
        BASE_DIR= os.path.dirname(os.path.abspath(__file__))
        save_image_dir=os.path.join(BASE_DIR, "../Users")
        self.user=user
        for f in f_faces:
            f_split=str(f).replace("'","").split(",")
            try:
                f_x=f_split[0]
                f_y=f_split[1]
                f_w=f_split[2]
                f_h=f_split[3]
                roi_color=self.frame[int(f_y):int(f_y)+int(f_h), int(f_x):int(f_x)+int(f_w)]
                self.user_name=get_user_from_stream(self.frame)
                if (self.user_name == self.user):
                    t=time.strftime("%Y%m%d%H%M%S")
                    new_file_count=count_pics_for_user(self.user)
                    while (new_file_count >= 100):
                        last_mod_file=Work_with_files.get_last_mod_file(save_image_dir+"/"+self.user_name)
                        Work_with_files.remove_file(last_mod_file)
                        new_file_count=count_pics_for_user(self.user)
                    img_item2=save_image_dir+"/"+user+"/"+user+"_"+t+".png"

                    #save the image
                    cv2.imwrite(img_item2, roi_color)
            except Exception as e:
                print(e)
                continue