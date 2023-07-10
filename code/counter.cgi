#!"C:\xampp\perl\bin\perl.exe"
use CGI;

# カウンタのファイルパス
my $counter_file = './data/counter.txt';  # カウンタのファイルパスを適宜変更してください

# カウンタの初期値を設定
my $counter = read_counter_from_file($counter_file) || 0;

# カウンタのインクリメント
$counter++;

# カウンタをファイルに保存
write_counter_to_file($counter_file, $counter);

# CGIオブジェクトの作成
my $cgi = CGI->new;

# レスポンスのヘッダを出力
print $cgi->header('text/html');

# レスポンスのボディを出力
print "<html>\n";
print "<head><title>Counter</title></head>\n";
print "<body>\n";
print "<h1>Counter</h1>\n";
print "<p>This page has been loaded $counter times.</p>\n";
print "</body>\n";
print "</html>\n";

# カウンタの値をファイルから読み込むサブルーチン
sub read_counter_from_file {
    my ($file) = @_;
    if (-e $file) {
        open(my $fh, '<', $file) or die "Failed to open counter file: $!";
        my $counter = <$fh>;
        close($fh);
        chomp($counter);
        return $counter;
    }
    return undef;
}

# カウンタの値をファイルに保存するサブルーチン
sub write_counter_to_file {
    my ($file, $counter) = @_;
    open(my $fh, '>', $file) or die "Failed to open counter file: $!";
    print $fh $counter;
    close($fh);
}