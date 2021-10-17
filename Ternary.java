class Ternary
{
    public static void main(String []args)
    {
        int a=9,b=6,c=45;
        //c=a>b?a:b;
        if(a>b && a>c)
        System.out.println("Greater value is"+a);
        else if(b>c)
        System.out.println("Greater value is"+b);
        else
          System.out.println("Greater value is"+c);


    }
}