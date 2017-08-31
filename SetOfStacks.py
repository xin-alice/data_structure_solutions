public class SetOfStacks{
ArrayList<Stack> stacks = new ArrayList<Stack>()
public int capacity;
public SetOfStacks(int capacity){
this.capacity = capacity;}

public getLastStack(){
if(stacks.size()==null) return null;
else{
return stacks.get(stacks.size()-1);}
}

public boolean isEmpty(){
Stack last = getLastStack();
return last ==null;
}


public void push(int v){
Stack last = getLastStack();
if(last != null && !last.isFull()){
last.push(v);}
else{Stack stack = new Stack(capacity);
stack.push(v);stacks.add(stack);}
}

public int pop(){
Stack last = getLastStack();
if (last == null)throw new EmptyStackException();
v = last.pop();
if(last.size ==0) stacks.remove(stacks.size()-1);
return v;}


}