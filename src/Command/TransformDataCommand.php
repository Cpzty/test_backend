<?php
namespace App\Command;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

class TransformDataCommand extends Command
{
    protected static $defaultName = 'app:transform-data';

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $output->writeln('Starting JSON → CSV transformation...');

        // 1. Get JSON file
        date_default_timezone_set($_ENV['APP_TIMEZONE'] ?? 'UTC'); 
        $date = date('Ymd'); 
        $jsonFile = __DIR__ . '/../../var/data/data_' . $date . '.json';
        $csvFile = __DIR__ . '/../../var/data/ETL_' . $date . '.csv';

        if (!file_exists($jsonFile)) {
            $output->writeln('<error>JSON file not found: ' . $jsonFile . '</error>');
            return Command::FAILURE;
        }

        $jsonData = json_decode(file_get_contents($jsonFile), true);

        if ($jsonData === null) {
            $output->writeln('<error>Invalid JSON data</error>');
            return Command::FAILURE;
        }

        // 2. Open CSV file for writing
        if (!is_dir(dirname($csvFile))) {
            mkdir(dirname($csvFile), 0777, true);
        }

        $fp = fopen($csvFile, 'w');

        // 3. Write header row (based on first JSON element keys)
        if (isset($jsonData[0]) && is_array($jsonData[0])) {
            fputcsv($fp, array_keys($jsonData[0]));
        }

        // 4. Write data rows
        foreach ($jsonData as $row) {
            if (is_array($row)) {
                fputcsv($fp, $row);
            }
        }

        fclose($fp);

        $output->writeln('<info>CSV saved as ' . $csvFile . '</info>');
        $output->writeln('Done');

        return Command::SUCCESS;
    }
}
