use strict;
use warnings;

my @keys = sort keys %ENV;

foreach my $key (@keys) {
    my $value = $ENV{$key};
    print "$key: $value\n";
}