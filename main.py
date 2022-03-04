package tictactoe

import kotlin.math.abs

fun main() {
    val game = mutableListOf(
        mutableListOf(' ', ' ', ' '),
        mutableListOf(' ', ' ', ' '),
        mutableListOf(' ', ' ', ' ')
    )
    printGameBoard(game)
    var player = 0
    while (true) {
        if (state(game) == "X wins" || state(game) == "O wins" || state(game) == "Draw") {
            print(state(game))
            break
        }
        try {
            print("Enter the coordinates: ")
            val coordinates = readLine()!!.split(" ")
            val x = coordinates[0].toInt() - 1
            val y = coordinates[1].toInt() - 1

            if ((x < 0 || x > 2) || (y < 0 || y > 2)) {
                println("Coordinates should be from 1 to 3!")
            } else if (game[x][y] != ' ') {
                println("This cell is occupied! Choose another one!")
            } else {
                if (player % 2 == 0) {
                    game[x][y] = 'X'
                } else if (player % 2 == 1) {
                    game[x][y] = 'O'
                }
                player++
                printGameBoard(game)
            }
        } catch (e: NumberFormatException) {
            println("You should enter numbers!")
        }
    }
}

private fun state(game: MutableList<MutableList<Char>>): String {
    val a = game.flatMap { mutableList: MutableList<Char> -> mutableList.toList() }
    val xs = a.count { c -> c == 'X' }
    val os = a.count { c -> c == 'O' }
    val dashs = a.count {c -> c == ' '}
    if (abs(xs - os) > 1) {
        return "Impossible"
    } else if (isCharWon('X', a) && isCharWon('O', a)) {
        return "Impossible"
    } else if (isCharWon('X', a)) {
        return "X wins"
    } else if (isCharWon('O', a)) {
        return "O wins"
    } else if (dashs > 0) {
        return "Game not finished"
    } else {
        return "Draw"
    }
}

private fun printGameBoard(game: MutableList<MutableList<Char>>) {
    println("---------")
    println("| ${game[0][0]} ${game[0][1]} ${game[0][2]} |")
    println("| ${game[1][0]} ${game[1][1]} ${game[1][2]} |")
    println("| ${game[2][0]} ${game[2][1]} ${game[2][2]} |")
    println("---------")
}

private fun isCharWon(c: Char, pattern: List<Char>): Boolean {
    return pattern[0] == c && pattern[1] == c && pattern[2] == c ||
        pattern[3] == c && pattern[4] == c && pattern[5] == c ||
        pattern[6] == c && pattern[7] == c && pattern[8] == c ||
        pattern[0] == c && pattern[3] == c && pattern[6] == c ||
        pattern[1] == c && pattern[4] == c && pattern[7] == c ||
        pattern[2] == c && pattern[5] == c && pattern[8] == c ||
        pattern[0] == c && pattern[4] == c && pattern[8] == c ||
        pattern[2] == c && pattern[4] == c && pattern[6] == c
}
