package model;

import java.time.LocalDateTime;

public class SortingTask extends Task{
    private String message;
    private String from;
    private String to;
    private LocalDateTime date;
    private String metoda;
    private int[] array;

    private class BubbleSort {
        void bubbleSort(int arr[])
        {
            int n = arr.length;
            for (int i = 0; i < n - 1; i++)
                for (int j = 0; j < n - i - 1; j++)
                    if (arr[j] > arr[j + 1]) {
                        // swap arr[j+1] and arr[j]
                        int temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
        }

        /* Prints the array */
        void printArray(int arr[])
        {
            int n = arr.length;
            for (int i = 0; i < n; ++i)
                System.out.print(arr[i] + " ");
            System.out.println();
        }

        // Driver method to test above
//        public static void main(String args[])
//        {
//            BubbleSort ob = new BubbleSort();
//            int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
//            ob.bubbleSort(arr);
//            System.out.println("Sorted array");
//            ob.printArray(arr);
//        }
    }

    private class QuickSort {

        // A utility function to swap two elements
        void swap(int[] arr, int i, int j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

        /* This function takes last element as pivot, places
           the pivot element at its correct position in sorted
           array, and places all smaller (smaller than pivot)
           to left of pivot and all greater elements to right
           of pivot */
        int partition(int[] arr, int low, int high)
        {

            // pivot
            int pivot = arr[high];

            // Index of smaller element and
            // indicates the right position
            // of pivot found so far
            int i = (low - 1);

            for (int j = low; j <= high - 1; j++) {

                // If current element is smaller
                // than the pivot
                if (arr[j] < pivot) {

                    // Increment index of
                    // smaller element
                    i++;
                    swap(arr, i, j);
                }
            }
            swap(arr, i + 1, high);
            return (i + 1);
        }

        /* The main function that implements QuickSort
                  arr[] --> Array to be sorted,
                  low --> Starting index,
                  high --> Ending index
         */
        void quickSort(int[] arr, int low, int high)
        {
            if (low < high) {

                // pi is partitioning index, arr[p]
                // is now at right place
                int pi = partition(arr, low, high);

                // Separately sort elements before
                // partition and after partition
                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);
            }
        }

        // Function to print an array
        void printArray(int[] arr, int size)
        {
            for (int i = 0; i < size; i++)
                System.out.print(arr[i] + " ");

            System.out.println();
        }

        // Driver Code
//        public static void main(String[] args)
//        {
//            int[] arr = { 10, 7, 8, 9, 1, 5 };
//            int n = arr.length;
//
//            quickSort(arr, 0, n - 1);
//            System.out.println("Sorted array: ");
//            printArray(arr, n);
//        }
    }

    public SortingTask(String taskId, String description, String message, String from, String to, LocalDateTime date,String metoda, int[] array) {
        super(taskId,message);
        this.message = message;
        this.from = from;
        this.to = to;
        this.date = date;
        this.metoda = metoda;
        this.array = array;

        if(metoda.equals("BubbleSort")){
            BubbleSort ob = new BubbleSort();
            ob.bubbleSort(array);
//            ob.printArray(array);
        }
        else if(metoda.equals("QuickSort")){
            QuickSort qs = new QuickSort();
            int n = array.length;
            qs.quickSort(array,0,n-1);
//            qs.printArray(array,n);
        }
        else{
            System.out.println("Metoda aleasa nu se afla in lista");
        }

    }
    @Override
    public void execute() {
        System.out.println("Metoda aleasa: " + metoda);
        for(int i = 0; i<this.array.length;i++)
            System.out.print(this.array[i] + " ");
        System.out.println();
    }
}
