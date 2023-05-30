import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int sum = 0;
		for (int i=0; i<5; i++) {
			int ipt = Integer.parseInt(br.readLine());
			if (ipt < 40) {
				ipt = 40;
			}
			sum = sum + ipt;
		}
		System.out.println(sum / 5);
	}
}