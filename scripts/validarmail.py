mail = " "
print("Introduce un mail:")
mail = input()

if mail.find("@") == -1:
    print("Error, el mail no contiene @")
elif (mail.find(".") == -1) :
    print("Error, el mail no contiene .")
elif (mail[0] == "@") or (mail[0] == ".") or (mail[len(mail)-1] == "@") or (mail[len(mail)-1] == "."):
    print("Error, el mail no puede empezar o acabar con @ o .")
elif (mail.find("@") != mail.rfind("@")):
    print("Error, el mail no puede contener más de una @")
elif mail.find("@") > mail.rfind("."):
    print("Error, no hay un punto tras la @ para marcar el dominio")
elif (len(mail[mail.rfind(".") + 1:]) < 2) or (len(mail[mail.rfind(".") + 1:]) > 4) :
    print("Error, dominio de longitud incorrecta")
else:
    print("Mail correcto")