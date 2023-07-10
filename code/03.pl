use strict;
use warnings;

sub above_average{
  my $ave = ($_[0] + $_[1]+ $_[2]+ $_[3]+ $_[4]+ $_[5]) / 6;
  my @return_list;

    for(my $i=0; $i<6 ; $i++){
        if($ave < $_[$i]){
                push(@return_list, $_[$i])
            }
        }
    
    print "ave: $ave\n";
  return @return_list;
}

my @result = &above_average(10, 80, 32, 58, 13, 3);

print "@result\n";