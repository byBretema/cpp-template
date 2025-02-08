#include <span>

#include "Utils/base.hpp"
#include "Utils/args.hpp"

int main(int argc, char *argv[])
{
    fmt::println("");

    //---------------------------------
    //--- ARGS
    //---------------------------------

    // Define
    auto &cli = _args::init("Test", "0.0.1", "Built @byBretema");
    cli.add_argument("Num").help("Meaning of life").scan<'d', int32_t>();

    // Parse
    if (!_args::parse(cli, argc, argv))
    {
        return -1;
    }

    // Gather values
    int32_t num = cli.get<int32_t>("Num");

    //---------------------------------
    //--- MAIN
    //---------------------------------

    fmt::println("The input value was: {}", num);

}
