public class ThreadAufgabe {
    public static void main(String[] args) {
        int limit = 1000; 
        Thread gerade = new Thread(new GeradeRunn(limit));
        gerade.start();

        Thread ungerade = new Thread(new UngeradeRunn(limit));
        ungerade.start();
    }
}

class GeradeRunn implements Runnable {
    private int limit;

    public GeradeRunn(int limit) {
        this.limit = limit;
    }

    @Override
    public void run() {
        for (int i = 0; i <= limit; i += 2) {
            System.out.println("Gerade: " + i);
        }
    }
}

class UngeradeRunn implements Runnable {
    private int limit;

    public UngeradeRunn(int limit) {
        this.limit = limit;
    }

    @Override
    public void run() {
        for (int i = 1; i <= limit; i += 2) {
            System.out.println("Ungerade: " + i);
        }
    }
}
