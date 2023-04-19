package com.wordcount;

import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

/*
 * 
 * Driver class extends the Configured class to obtain hadoop cluster
 * configurations, the tool implementation kick starts the mapreduce ops
 */
public class Driver extends Configured implements Tool{

    /**
     * 
     * Define config for the mapreduce job i.e  map and reduce classes, inputs 
     * and outputs of the map reduce
     */
    @Override
    public int run(String[] arg0) throws Exception {
        /*
         * 
         * Retrieve configuration for the mapreduce job
         */
        Job job = Job.getInstance(getConf());
        job.setJobName("Word Count");
        job.setJarByClass(getClass());

        /*
         * Explicitly define the output of map and reduce jobs
         */
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(LongWritable.class);

        /**
         * Define names for map and reduce operations
         */
        job.setMapperClass(Map.class);
        job.setReducerClass(Reduce.class);

        /*
         * Define where the input and output file are to be obtained
         * Will be passed out as command line arguments from shell
         */
        Path inputFilePath = new Path(arg0[0]);
        Path outputFilePath = new Path(arg0[1]);

        /*
         * 
         * Configure the file input and output specifications
         */
        FileInputFormat.addInputPath(job,inputFilePath);
        FileOutputFormat.setOutputPath(job,outputFilePath);

        /*
         * Return true if job has compeleted successfully
         */
        return job.waitForCompletion(true) ? 0 : 1;
    }

    public static void main(String[] args) throws Exception{
        int exitCode = ToolRunner.run(new Driver(),args);
        System.exit(exitCode);
    }
    
}
