use strict;
use warnings;

while(1){
    print "input> ";
    my $in = <STDIN>;
    chomp($in);

    last if $in eq " "; 

    if ($in =~ /^[01]+5$/) {
        print "accepted\n";
    } else {
        print "not accepted\n";
    }
} 


