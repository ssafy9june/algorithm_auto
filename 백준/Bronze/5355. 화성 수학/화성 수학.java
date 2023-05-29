import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String [] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			String line = br.readLine();
			String [] arr = line.split(" ");
			double num = Double.parseDouble(arr[0]);
			for (int j=1; j<arr.length; j++) {
				if (arr[j].equals("@")) {
					num = num * 3;
				} else if(arr[j].equals("%")) {
						num = num + 5;
					} else {
						num = num - 7;
					}
				}
			System.out.printf("%.2f\n", num);
			}
			
		}
	}