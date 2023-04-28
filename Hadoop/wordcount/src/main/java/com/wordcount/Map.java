package com.wordcount;

/*
 * Import dependancies
 */
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

/*
 * Mapper class throws IO exception
 */
import java.io.IOException;

/* Map class extends the mapper class which has an implementation of
    the map method
    1st arg : Input key is the line number of type Long
 * 2nd arg : Input value is of type text
 * 3rd and 4th args : Output is collection of key value pairs,i.e Key is each word in input 
 * and value will be the occurance of the word always one
 */
public class Map extends Mapper<LongWritable, Text, Text, IntWritable>{

    /*
     * 
     * Called once for each key value input pair i.e line record
     * Key and Value parama corresponds to the 1st and 2nd args passed to the class
     * The context endable the mapper to interract with rest of the hadoop system.
     */
    @Override
    public void map(LongWritable key, Text value,Context context)
            throws IOException,InterruptedException{
            
            /*
             * 
             * Converst each input line to a string
             * Create an array of the words separated by a space
             * in the input string
             */
            String line = value.toString();
            String[] words = line.split(" ");
            
            /*
             * 
             * Iterate through the input array this sets the output of the loop
             * function as every occurance of every word as the key together with a count of one
             * as the value. 
             */
            for(String word : words){
                context.write(new Text(word),new IntWritable(1));
            }

        }
    
}
