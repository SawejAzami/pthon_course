// import java.util.Scanner;

//  class Temple {
//     public static void pattern(int n) {
//         // top part
//         for (int i = 1; i <= n; i++) {
//             for (int j = 1; j <= i; j++) {
//                 System.out.print("*");
//             }
//             // space left top
//             for (int j = n - 1; j >= i; j--) {
//                 System.out.print(" ");
//             }

//             // space top left and n==i pr @
//             if (i == n) {
//                 for (int j = 1; j <= n; j++) {
//                     System.out.print("@");
//                 }
//             } else {
//                 for (int j = 1; j <= n; j++) {
//                     System.out.print(" ");
//                 }
//             }

//             // // right part space
//             for (int j = n; j > i; j--) {
//                 System.out.print(" ");
//             }
//             // // right start
//             for (int j = 1; j <= i; j++) {
//                 System.out.print("*");
//             }

//             System.out.println();
//         }

//         // Now bottome part
//         for (int i = 1; i <= n - 1; i++) {
//             for (int j = 1; j <= n; j++) {
//                 System.out.print(" ");

//             }
//             for (int j = 1; j <= n; j++) {
//                 System.out.print("@");
//             }

//             System.out.println();
//         }

//         for(int i=1;i<=n/2+1;i++){
//             for(int j=1;j<=n;j++){
//                 System.out.print(" ");
//             }
//             for(int j=1;j<i;j++){
//                 System.out.print(" ");
//             }
//             for(int j=n/2+1;j>=i;j--){
//                 System.out.print("*");
//             }
//             for(int j=n/2+1;j>i;j--){
//                 System.out.print("*");
//             }
//            System.out.println();
//         }
//     }

//     public static void main(String[] args) {
//         int n;
//         Scanner sc = new Scanner(System.in);
//         System.out.println("Enter a number");
//         n = sc.nextInt();
//         pattern(n);
//         sc.close();
//     }
// }


import java.util.Scanner;

 class RamBaan {
    public static void pattern(int n){
        //  row print
        for(int i=1;i<=n;i++){
            // top-left
            for(int j=1;j<=i;j++){
                    System.out.print("*");         
            }
             
            // Space mid upper
            for(int j=i;j<=(n*2)-1;j++){
                if(i!=n){
                     System.out.print(" ");
                }
            }
            // upper single *
            if(i==n-1){
                System.out.print("*");
            }
            // middle line extra two star
            if(i==n){
                for(int j=1;j<=n;j++){
                    System.out.print("*");
                }
                System.out.print("");
            }
            System.out.println();
        }
        // now bottom part
        for(int i=n-1;i>=1;i--){
            for(int j=i;j>=1;j--){
                System.out.print("*");
            }
            if(i==n-1){
                for(int j=1;j<=n*2-i;j++){
                    System.out.print(" ");
                }
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        int n;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number");
        n=sc.nextInt();
        pattern(n);
        sc.close();
    }
}