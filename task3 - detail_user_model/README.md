# Detail User Model


api/user/ -> Burda IsAuthenticated olan istifadəçilər bütün Userləri görə bilir. Admin olan userlər yeni user də əlavə edə bilər

api/user/pk/ -> Burada IsAuthenticated olan istifadeçilər detail view görə bilir. Əgər user öz profilidirsə onu edit edə bilir. Və ya is_superuser sorğusuna cavab verən istifadəçi bütün userləri edit edə bilir
