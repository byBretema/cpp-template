#pragma once

#include <argparse/argparse.hpp>  //! https://github.com/p-ranav/argparse?tab=readme-ov-file#table-of-contents

#include "base.hpp"

namespace _args
{
    using CLI = argparse::ArgumentParser;

    [[nodiscard]] CLI &init(const std::string &title, const std::string &version, const std::string &description);
    [[nodiscard]] bool parse(CLI &cli, int argc, char *argv[]);

}  // namespace cli
