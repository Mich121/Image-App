# Image-App
Technologies: Python + Django + REST Framework + HTML + Bootstrap + CSS
<hr>
--------------------------DOCKER--------------------------
step to download unit of app:</br>
1.docker pull 375162749183/image_app </br> 
2.docker run --rm -p 8000:8000 --name container_name image_id </br>
3.and enter to: http://127.0.0.1:8000/ </br>
<hr>
In this app users are divided into three types: basic, premium and enterprise.</br>
Each type has some special functionality. For instance basic can list their image and make 200x200 thumbnails.</br>
Premium and Enterprise also can make 400x400 thumbnails and see link to originally uploaded image. </br>
Admin additionaly can make thumbnails with configurable dimension.
In dockerize unit of app, you will have sqlite data base. There you will have saved superuser that I had created.</br>
username: admin</br>
password: admin</br>
<hr>
