import java.util.ArrayList;
import java.util.Collections;

public class ModifyStringArrayListImpl implements ModifyStringArrayList {
    @Override
    public ArrayList<String> listeUmdrehen(ArrayList<String> inputList) {
        Collections.reverse(inputList);
        return inputList;
    }

    @Override
    public ArrayList<String> listeMischen(ArrayList<String> inputList) {
        Collections.shuffle(inputList);
        return inputList;
    }

    @Override
    public String listeMaxElement(ArrayList<String> inputList) {
        return Collections.max(inputList);
    }

    @Override
    public String listeMinElement(ArrayList<String> inputList) {
        return Collections.min(inputList);
    }
}
