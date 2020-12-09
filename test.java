// class Solution {
//     public static int longestPalindrome(String s) {
//         final int[] arr = new int[128];
//         for (final char c : s.toCharArray()) {
//             arr[c]++;
//         }
//         System.out.println(arr);
//         int count = 0;
//         for (final int i : arr) {
//             count += (i % 2);
//         }
//         System.out.println(count);
//         return count == 0 ? s.length() : (s.length() - count + 1);
//     }

//     public  static void main(final String[] args){
//         int r=longestPalindrome("abccccdd");
//         // System.out.print(r);
//     }
// }

class Demo {

    public static void main(String[] args) {
        int[] arr = new int[128];
        String str = "helloworld";
        char[] data = str.toCharArray();// 将字符串转为数组
        for (int x = 0; x < data.length; x++) {
            System.out.print(data[x] + " ");
        }
        // System.out.println(new String(data));
        System.out.println();
        for (char c:str.toCharArray()){
            arr[c]++;
            System.out.print(arr[c]+" ");
        }
        System.out.println();
        for (char c:str.toCharArray()){
            System.out.print(c+" ");
        }
        System.out.println(Arrays.toString(arr));
    }
}