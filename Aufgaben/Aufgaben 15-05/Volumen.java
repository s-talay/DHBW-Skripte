public class Volumen {
	public static void main(String[] args) {
		new Volumen();
	}
	
	public double masse = 123;
	public double vol = 1234;
	double dichte;
	
	public Volumen() {
		if(vol == 0) {
			System.err.println("Volumen kann nicht 0 sein");
		}else if(vol < 0) {
			System.err.println("Volumen kann nicht negativ sein");
		}else if(vol > 1000) {
			System.err.println("Volumen ist zu groß");
		}else {
			dichte = masse/vol;
			System.out.println("Dichte: "+dichte);
		}
	}
}