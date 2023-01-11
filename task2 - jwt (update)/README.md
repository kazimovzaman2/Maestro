Burda iki app yaratdim:

1: app

  burda dj_rest_auth kitabxanasindan istifade etdim. Hazir endpoint'lərdən istifadə etmək olur. 
   auth/registration qeydiyyat üçün endpointdir.
   auth/password/change/ şifrəni dəyişmək üçün endpointdir.
   
   
2: main
  Burda AbstractUser'dən istifadə edərək UserData modeli yaratdım. Postmandan istifadə edərək qeydiyyatdan keçə, şifrəni dəyişdirə, useri update etmək olur.
    user/api/register/
    user/api/password/change/
    user/api/updateuser/
