use strict;
use warnings;

my @week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
my @input_list;

print "index> \n";

while (1){
    my $num = <STDIN>;
    chomp $num;
    #空白が入力されたら終了
    last if $num eq " "; 
    push @input_list, $num;
}

#昇順にソート
@input_list = sort { $a <=> $b } @input_list;

#各整数値に対応する曜日を出力
foreach my $num (@input_list) {
    print "week[$num]: $week[$num]\n";
}
