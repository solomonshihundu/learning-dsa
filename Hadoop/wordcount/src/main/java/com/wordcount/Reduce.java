package com.wordcount;

/*
 * Import dependancies
 */
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

/*
 * Mapper class throws IO exception
 */
import java.io.IOException;

/*
 * 
 * The Reduce class extends the reducer class which and overrides the reduce method
 * 1st and 2nd args: Inputs consist of a collection of keys and values pairs,common keys grouped together by shuffle operation
 * 3rd and 4th atgs : Outputs consist of the unique input keys and there counts 
 * 
 */
public class Reduce extends Reducer<Text,IntWritable,Text,LongWritable>{
    /*
     * 
     * Called once for each distinct key from the shuffle phase
     * Keys are the distinct words from input file
     * values are the collection of ones whose length correspond to
     * the number of occurance.
     * Context enables us to write out the output
     */
    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
    throws IOException,InterruptedException{
        int count=0;
        /*
         * Iterate through the collection of values
         * increate the count variable with every iteration thus
         * the final count would translate to the number of occurance of
         * each word
         */
        for(IntWritable value : values){
            count++;
        }
        context.write(key,new LongWritable(count));
    }
    
}
