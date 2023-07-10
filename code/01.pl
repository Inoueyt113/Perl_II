use strict;
use warnings;

print "start> ";
chomp(my $start = <STDIN>);
print "end> ";
chomp(my $end = <STDIN>);
print "result: ";

my $sum = 0;
while($start <= $end){
    $sum += $start;
    $start++;
}

print $sum;

