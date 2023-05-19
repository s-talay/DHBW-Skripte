public class HashFunktionen {
	private static final int S_0 = 0x332e2800; // in ASCII == ROFL

	public static void main(String[] args) {
//		test();
		System.out.printf("%x\n",H("efghijk".getBytes()));
	}

	static int H(byte[] data) {
		int state = S_0;
		int buffer = 0;
		int count = 0;

		int i = 0;
		while (i < data.length) {
			// Puffer füllen
			buffer |= (data[i]) << (24 - (count * 8));
			count++;
			i++;
			if (count == 4) { // Wenn Puffer voll
				state = Q(state ^ buffer);
				buffer = 0;
				count = 0;
			}
		}
		// Fertig

		// Auffüllen?
		long padding = 0xFFFFFFFFL;
//		printHex("count",count);
//		printHex("buffer",buffer);
//		printHex("state",state);

		if (buffer != 0) {// Buffer noch mit Daten?
//			buffer = buffer<<(8*count);
//			printHex("count", count);
//			printHex("padding vorher", padding);
			buffer |= (padding >> (8 * count)); // count = 1; buffer = 0x41000000
			// 0xFFFFFFFF >> 8 = 0x00FFFFFF
			// 0x41FFFFFF
//			printHex("padding nachher", buffer);
			state = Q(state ^ buffer);
			buffer = 0;
			count = 0;
		}
//		printHex("state",state);
		// letztmalig
		state = Q(state ^ buffer);
//		printHex("state",state);
		return state;
	}

	static int Q(int input) {
		int rotated = rotLeft(input, 17);
		return input ^ rotated;
	}

	static void test() {
		int q1 = Q(S_0);
		System.out.println("q1: " + String.format("%08x", q1));
		int q2 = Q(Q(S_0));
		System.out.println("q2: " + String.format("%08x", q2));
		int q3 = Q(Q(Q(S_0)));
		System.out.println("q3: " + String.format("%08x", q3));
		
		
		int h1 = H("".getBytes());
		System.out.println("h1: " + String.format("%08x", h1));
		int h2 = H("A".getBytes());
		System.out.println("h2: " + String.format("%08x", h2));
		int h3 = H("AB".getBytes());
		System.out.println("h3: " + String.format("%08x", h3));
		int h4 = H("ABC".getBytes());
		System.out.println("h4: " + String.format("%08x", h4));
		int h5 = H("ABCD".getBytes());
		System.out.println("h5: " + String.format("%08x", h5));
		int h6 = H("ABCDE".getBytes());
		System.out.println("h6: " + String.format("%08x", h6));

	}

	static int rotLeft(int num, int rot) {
		return (num << rot) | (num >>> (32 - rot));
	}
//	void printHex(String what, long padding){
//		System.out.println(what +": "+String.format("%08x", padding));
//	}
//	void printHex(String what, int padding){
//		System.out.println(what +": "+String.format("%08x", padding));
//	}
}
