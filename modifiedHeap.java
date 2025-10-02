/*
Create a class that creates a bllueprint to use a modified heap that has 2^x children.
Define a constructor Methos
Define a Insert Method
Define a Pop Method
*/

import java.util.ArrayList;

public class modifiedHeap<T extends Comparable<T>> {
  int power;  // atribuyte that hs the vakue of x
  ArrayList<T> heap;
  int size;

  public modifiedHeap() { // Create a class constructor for the modifiedHeap class
    power = 1;  // Set the initial value for the class attribute x
    size = 10;
    heap = new ArrayList<>();
  }
  
  public modifiedHeap(int power) { // Create a class constructor with power given as a parameter for the modifiedHeap class
    this.power = power;  // Set the initial value for the class attribute x
    size = 10;
    heap = new ArrayList<>();
  }

  private int Parent(int i) {
    if (i == 0) {
        return -1;
    }
    if (i > size) {
        return -1;
    }
    return (int)((i -1)/ Math.pow(2,power));
  }

  public void SiftUp(int i) {
    while ((i > 0) & (heap.get(i).compareTo(heap.get(Parent(i))) > 0)) {
    // if (heap.get(i).compareTo(heap.get(Parent(i))) > 0) {
    T temp = heap.get(i);
    heap.set(i, heap.get(Parent(i)));
    heap.set(Parent(i), temp);
    i = Parent(i);
    // }
    }
  }

  public void Insert(T value) {
    heap.add(value);
    size += 1;
    if (size == 1) {
        return;
    }
    SiftUp(size-1);
  }

  private void shiftdown(int i) {
    while((i < size) && (heap.get(i).compareTo((t))))
  }

  public void Popmax() {
    if (!heap.isEmpty()) {
      T temp = heap.get(size - 1);
      heap.remove(heap.size() - 1);
      size -= 1;
      heap.set(0,temp);
      if (size > 1) {
        shiftdown(0);
      }
    }  
  }


  public static void modifiedHeap(String[] args) {
    Main myObj = new Main();
    System.out.println(myObj.x);
  }
}
