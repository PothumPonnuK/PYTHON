class PRACTICEfile():
    def Subfields():
        lists=["Sub-fields in AI are:","Machine Learning","Neural Network","Vision","Robotics","Speech Processing","Natural Language Processing"]
        
        for name in lists:
            print(name)
     
    def OddEven():
            whether=int(input("Enter a number:"))
            if whether%2!=0:
                print(whether,"is Odd number")
            else:
                print(whether,"is Even number")
                
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if age>=21:
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
            
            
          
        
      
      
            
    def percentage():
        tam=98
        print("Subjects1=",tam)
        eng=87
        print("Subjects2=",eng)
        maths=95
        print("Subjects3=",maths)
        scie=95
        print("Subjects4=",scie)
        social=93
        print("Subjects5=",social)
        add=tam+eng+maths+scie+social
        print("Total:",add)
        percentage=(add/500)*100
        print("Percentage:",percentage)
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        Areaformula=(height*breadth)/2
        print("Aera of triangle:",Areaformula)
        a=2
        print("Height1:",a)
        b=4
        print("Height2:",b)
        c=4
        print("Breadth:",c)
        add=a+b+c
        print("Perimeter of Triangle:",add)
        
                      