#!/usr/bin/env perl -w

use strict;
use warnings;

my $time_sum=0;
my $time_count=0;
my $time_min;
my $time_max;

my $best=0;

my $ref = shift;

while (<>){
#print $_;
  if (m/'cost':\s*([0-9]+)/) {
    $best = $1;
    next;
  }
  if (m/time:\s*([0-9.]+)/) {
    my $t=$1;
    $time_count++;
    
    $time_sum += $t;
    if (not defined $time_max ){
      $time_max = $t;
    }
    if (not defined $time_min ){
      $time_min = $t;
    }
    
    if ($t>$time_max) {
      $time_max = $t;
    }
    if ($t<$time_min) {
      $time_min = $t;
    }
  }
}

printf "%d & %0.2f & %0.2f   & %0.2f  & %0.2f \n", $best, ($ref-$best)*100.0/$ref, $time_sum/$time_count, $time_max, $time_min;
