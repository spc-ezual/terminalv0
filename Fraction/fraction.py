class fraction:


    def __init__(self,nomi,deno):
        i=2
        while i<=nomi and i<=deno:
            if nomi%i==0 and deno%i==0:
                nomi=nomi//i
                deno=deno//i
            else:
                i=i+1
        self.nomi=nomi
        self.deno=deno


    def addition_entier(self,en):
        add=self.nomi+self.deno*en
        i=2
        copy_deno=self.deno
        while i<=add and i<=copy_deno:
            if  add%i==0 and copy_deno%i==0:
                add=add//i
                copy_deno=copy_deno//i
            else:
                i=i+1
        if nomi%deno==0:
            return [nomi//deno]

        add=str(add)+"/"+str(copy_deno)
        return [add]


    def addition_frac(self,nb2):
        copy_n1=self
        copy_n2=nb2

        nomi=copy_n1.nomi*copy_n2.deno+copy_n1.deno*copy_n2.nomi
        deno=copy_n1.deno*copy_n2.deno
        i=2
        while i<=nomi and i<=deno:
            if nomi%i==0 and deno%i==0:
                nomi=nomi//i
                deno=deno//i
            else:
                i=i+1
        if nomi%deno==0:
            return [nomi//deno]


        frac=str(nomi)+"/"+str(deno)
        return [frac]


    def sou_entier(self,en):
        add=self.nomi-self.deno*en
        i=2
        copy_deno=self.deno
        while i<=add and i<=copy_deno:

            if  add%i==0 and copy_deno%i==0:
                add=add//i
                copy_deno=copy_deno//i

            else:
                i=i+1

        if nomi%deno==0:
            return [nomi//deno]


        add=str(add)+"/"+str(copy_deno)
        return [add]


    def sou_frac(self,nb2):
        copy_n1=self
        copy_n2=nb2

        nomi=copy_n1.nomi*copy_n2.deno-copy_n1.deno*copy_n2.nomi
        deno=copy_n1.deno*copy_n2.deno
        i=2

        while i<=nomi and i<=deno:

            if nomi%i==0 and deno%i==0:
                nomi=nomi//i
                deno=deno//i

            else:
                i=i+1

        if nomi%deno==0:
            return [nomi//deno]


        frac=str(nomi)+"/"+str(deno)
        return [frac]


    def multi_entier(self,en):
        add=self.nomi*en
        i=2
        copy_deno=self.deno

        while i<=add and i<=copy_deno:

            if  add%i==0 and copy_deno%i==0:
                add=add//i
                copy_deno=copy_deno//i

            else:
                i=i+1

        if nomi%deno==0:
            return [nomi//deno]


        add=str(add)+"/"+str(copy_deno)
        return [add]


    def multi_frac(self,nb2):
        copy_n1=self
        copy_n2=nb2
        nomi=copy_n1.nomi*copy_n2.nomi
        deno=copy_n1.deno*copy_n2.deno
        i=2

        while i<=nomi and i<=deno:

            if nomi%i==0 and deno%i==0:
                nomi=nomi//i
                deno=deno//i

            else:
                i=i+1

        if nomi%deno==0:
            return [nomi//deno]


        frac=str(nomi)+"/"+str(deno)
        return [frac]


    def div_entier(self,en):
        add=self.demo*en
        i=2
        copy_nomi=self.nomi

        while i<=add and i<=copy_nomi:

            if  add%i==0 and copy_nomi%i==0:
                add=add//i
                copy_nomi=copy_nomi//i

            else:
                i=i+1

        if nomi%deno==0:
            return [nomi//deno]


        add=str(copy_nomi)+"/"+str(add)
        return [add]


    def div_frac(self,nb2):
        copy_n1=self
        copy_n2=nb2
        nomi=copy_n1.nomi*copy_n2.deno
        deno=copy_n1.deno*copy_n2.nomi
        i=2

        while i<=nomi and i<=deno:

            if nomi%i==0 and deno%i==0:
                nomi=nomi//i
                deno=deno//i

            else:
                i=i+1

        if nomi%deno==0:
            return [nomi//deno]


        frac=str(nomi)+"/"+str(deno)
        return [frac]

b=fraction(5,9)
a=fraction(75,8)




