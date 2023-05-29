import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String [] arr = br.readLine().split(" ");
		int [] nums = new int[3];
		for (int i=0; i<3; i++) {
			nums[i] = Integer.parseInt(arr[i]);
		}
		Arrays.sort(nums);
		System.out.println(nums[1]);
	}
}