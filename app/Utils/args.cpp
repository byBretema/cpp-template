#include "args.hpp"

namespace _args
{

//-----------------------------------------------------------------------------

[[nodiscard]] CLI &init(const std::string &title, const std::string &version, const std::string &description)
{
    static CLI cli(title, version);
    cli.add_description(description);
    return cli;
}

//-----------------------------------------------------------------------------

[[nodiscard]] bool parse(CLI &cli, int argc, char *argv[])
{
    try
    {
        cli.parse_args(argc, argv);
        return true;
    }
    catch (const std::exception &err)
    {
        fmt::println("{}", err.what());
        fmt::println("{}", cli.help().str());
        return false;
    }
}

//-----------------------------------------------------------------------------

}  // namespace omi::cli
