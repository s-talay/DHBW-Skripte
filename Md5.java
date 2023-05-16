package Main;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Test {
	static int upperLimit = 999999;
	public static void main(String[] args) {
		new Test();
	}
	public Test() {
		String name = "Seyfullah Talay ";
		int count = 0;
		int index = -1;
		for(int i = 0; i<upperLimit; i++) {
			String hash = md5(name+i);
			if(count == 0 && hash.startsWith("0000")) index = i;
			if(hash.startsWith("0000")) count++;
			System.out.println(hash);
		}
		System.out.println(count+" mal '0000'");
		System.out.println("Das erste Mal bei Index "+index);
	}
	String md5(String input) {
		MessageDigest md = null;
		try {
			md = MessageDigest.getInstance("MD5");
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
			return null;
		}
		md.update(input.getBytes());
		byte[] hash = md.digest();
		StringBuffer sb = new StringBuffer();
		for (byte b : hash) {
			String hex = Integer.toHexString(0xff & b);
			if (hex.length() == 1)
				sb.append('0');
			sb.append(hex);
		}
		return sb.toString();
	}
}
