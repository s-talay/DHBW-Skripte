import java.util.ArrayList;

public interface ModifyStringArrayList{

    /** @author Seyfullah,
     *  @param inputListe die zu ändernde Liste,
     *  @return umgedrehte Liste **/
    public ArrayList<String>listeUmdrehen(ArrayList<String> inputList);

      /** @author Seyfullah,
     *  @param inputListe die zu mischende Liste,
     *  @return gemischte Liste **/
    public ArrayList<String>listeMischen(ArrayList<String> inputList);

      /** @author Seyfullah,
     *  @param inputListe die Liste, deren größtes Element returnt werden soll,
     *  @return größtest Element **/
    public String listeMaxElement(ArrayList<String> inputList);

      /** @author Seyfullah,
     *  @param inputListe die Liste, deren kleinstes Element returnt werden soll,
     *  @return kleinstes Element **/
    public String listeMinElement(ArrayList<String> inputList);
    
}