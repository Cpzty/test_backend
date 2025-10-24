<?php

namespace App\Command;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Contracts\HttpClient\HttpClientInterface;

class FetchDailyDataCommand extends Command
{
    protected static $defaultName = 'app:fetch-daily-data';
    private $httpClient;

    public function __construct(HttpClientInterface $httpClient)
    {
        parent::__construct();
        $this->httpClient = $httpClient;
    }

    protected function configure()
    {
        $this
            ->setDescription('Fetches daily data from the API and saves as data_YYYYMMDD.json');
    }

    protected function execute(InputInterface $input, OutputInterface $output)
    {
        $apiUrl = 'https://dummyjson.com/users'; //API url

        $output->writeln('Fetching data from API...');

        try {
            $response = $this->httpClient->request('GET', $apiUrl);
            $data = $response->toArray();
        } catch (\Exception $e) {
            $output->writeln('<error>Error fetching API: '.$e->getMessage().'</error>');
            return Command::FAILURE;
        }

        date_default_timezone_set($_ENV['APP_TIMEZONE'] ?? 'UTC');
        $date = (new \DateTime())->format('Ymd');
        $filename = __DIR__ . '/../../var/data/data_' . $date . '.json';

        if (!is_dir(dirname($filename))) {
            mkdir(dirname($filename), 0755, true);
        }

        file_put_contents($filename, json_encode($data, JSON_PRETTY_PRINT));

        $output->writeln("Data saved to {$filename}");

        return Command::SUCCESS;
    }
}
