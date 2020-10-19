use strict;
use warnings;
use LWP::UserAgent;

my $base = 'https://www.uniprot.org';
my $tool = 'uploadlists';

my $params = {
  from => 'P_REFSEQ_AC',
  to => 'ENSEMBL_PRO_ID',
  format => 'tab',
  query => 'XP_013978521.1'
};

my $contact = ''; # Please set a contact email address here to help us debug in case of problems (see https://www.uniprot.org/help/privacy).
my $agent = LWP::UserAgent->new(agent => "libwww-perl $contact");
push @{$agent->requests_redirectable}, 'POST';

my $response = $agent->post("$base/$tool/", $params);

while (my $wait = $response->header('Retry-After')) {
  print STDERR "Waiting ($wait)...\n";
  sleep $wait;
  $response = $agent->get($response->base);
}

$response->is_success ?
  print $response->content :
  die 'Failed, got ' . $response->status_line .
    ' for ' . $response->request->uri . "\n";
