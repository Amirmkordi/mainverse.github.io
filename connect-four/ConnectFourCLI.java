/*
 * File: ConnectFourCLI.java
 * Compile: javac ConnectFourCLI.java
 * Run:     java ConnectFourCLI --time 12 --ai-first true --ansi true --anim true --anim-delay 40
 */
import java.util.*;
import java.io.*;
public class ConnectFourCLI {
    public static void main(String[] args) throws IOException {
        CliArgs cfg = CliArgs.parse(args);
        Game game = new Game(cfg);
        Renderer.printBanner(cfg.ansi); 
        Renderer.printHelp(game.board.cols);
        try (Scanner sc = new Scanner(System.in)) {
            while (true) {
                Renderer.render(game.board, -1, -1, 0, cfg.ansi);
                if (game.board.winner() != 0) {
                    System.out.println("Winner: " + (game.board.winner() == 1 ? "Human (X▲)" : "AI (O●)"));
                    System.out.println("Type 'new' to restart or 'q' to quit.");
                } else if (game.board.isFull()) {
                    System.out.println("Draw. Board is full.");
                    System.out.println("Type 'new' to restart or 'q' to quit.");
                }
                if (game.isAITurn() && game.board.winner() == 0 && !game.board.isFull()) {
                    Game.AIMove mv = game.aiMove();
                    animateDrop(game, mv.col, 2);
                    System.out.println("AI plays column " + (mv.col + 1) + " (score " + mv.score + ", depth " + mv.depth + ", " + mv.nodes + " nodes)");
                    continue;
                }
                System.out.print("> ");
                if (!sc.hasNextLine()) break;
                String line = sc.nextLine().trim();
                if (line.isEmpty()) continue;
                String[] parts = line.split("\\s+");
                String cmd = parts[0].toLowerCase(Locale.ROOT);
                if (cmd.equals("q") || cmd.equals("quit") || cmd.equals("exit")) {
                    System.out.println("Bye.");
                    break;
                } else if (cmd.equals("help")) {
                    Renderer.printHelp(game.board.cols);
                } else if (cmd.equals("new")) {
                    game.reset();
                    System.out.println("New game started.");
                } else if (cmd.equals("u") || cmd.equals("undo")) {
                    if (game.board.undo()) {
                        if (game.isAITurn()) {
                            if (!game.board.undo()) {
                                game.board.flipTurn();
                            }
                            System.out.println("Undid your last move and AI response.");
                        } else {
                            System.out.println("Undid last move.");
                        }
                    } else {
                        System.out.println("Nothing to undo.");
                    }
                } else if (cmd.equals("depth")) {
                    if (parts.length >= 2) {
                        try {
                            int d = Integer.parseInt(parts[1]);
                            game.depth = Math.max(1, Math.min(22, d));
                            System.out.println("AI fixed depth set to " + game.depth + " (set time 0 to use depth)");
                        } catch (NumberFormatException e) {
                            System.out.println("Usage: depth <int>");
                        }
                    } else {
                        System.out.println("AI depth: " + game.depth);
                    }
                } else if (cmd.equals("time")) {
                    if (parts.length >= 2) {
                        try {
                            int t = Integer.parseInt(parts[1]);
                            game.timeSeconds = Math.max(0, Math.min(60, t));
                            System.out.println("AI time per move set to " + game.timeSeconds + " second(s). (0 = fixed depth)");
                        } catch (NumberFormatException e) {
                            System.out.println("Usage: time <seconds>");
                        }
                    } else {
                        System.out.println("AI time per move (seconds): " + game.timeSeconds + " (0 = fixed depth)");
                    }
                } else if (cmd.equals("auto")) {
                    int steps = 1;
                    if (parts.length >= 2) {
                        try { steps = Math.max(1, Integer.parseInt(parts[1])); } catch (Exception ignored) {}
                    }
                    for (int i = 0; i < steps && game.board.winner() == 0 && !game.board.isFull(); i++) {
                        Game.AIMove mv = game.aiMove();
                        animateDrop(game, mv.col, 2);
                        System.out.println("Auto AI plays column " + (mv.col + 1) + " (score " + mv.score + ", depth " + mv.depth + ", " + mv.nodes + " nodes)");
                        Renderer.render(game.board, -1, -1, 0, game.cfg.ansi);
                    }
                } else if (isNumeric(cmd)) {
                    int col = Integer.parseInt(cmd) - 1;
                    if (game.board.currentPlayer != 1) {
                        System.out.println("Not your turn.");
                        continue;
                    }
                    if (col < 0 || col >= game.board.cols || game.board.heights[col] >= game.board.rows) {
                        System.out.println("Invalid move. Enter a column 1.." + game.board.cols + " that is not full.");
                        continue;
                    }
                    animateDrop(game, col, 1);
                    if (!game.humanMove(col)) {
                        System.out.println("Move failed.");
                    }
                } else {
                    System.out.println("Unknown command. Type 'help'.");
                }
            }
        }
    }
    private static void animateDrop(Game game, int col, int player) {
        if (!game.cfg.anim) return;
        int targetRow = game.board.rows - 1 - game.board.heights[col];
        for (int r = 0; r <= targetRow; r++) {
            Renderer.clearScreenIfAnsi(game.cfg.ansi);
            Renderer.render(game.board, r, col, player, game.cfg.ansi);
            try { Thread.sleep(Math.max(0, game.cfg.animDelayMs)); } catch (InterruptedException ignored) {}
        }
    }
    private static boolean isNumeric(String s) {
        for (int i = 0; i < s.length(); i++) if (!Character.isDigit(s.charAt(i))) return false;
        return !s.isEmpty();
    }
    static final class Game {
        final CliArgs cfg;
        int depth;
        int timeSeconds;
        final Board board;
        final AI ai;
        Game(CliArgs cfg) {
            this.cfg = cfg;
            this.depth = cfg.depth;
            this.timeSeconds = cfg.timeSeconds;
            this.board = new Board(cfg.rows, cfg.cols, 4);
            if (cfg.aiFirst) board.currentPlayer = 2;
            this.ai = new AI(cfg.cols);
        }
        void reset() {
            board.reset();
            board.currentPlayer = cfg.aiFirst ? 2 : 1;
            ai.clearStats();
        }
        boolean isAITurn() { return board.currentPlayer == 2; }
        boolean humanMove(int col) {
            if (board.currentPlayer != 1) return false;
            return board.play(col);
        }
        AIMove aiMove() {
            if (board.currentPlayer != 2) return new AIMove(-1, 0, 0, 0);
            AIMove mv = ai.search(board, depth, timeSeconds);
            if (mv.col >= 0) board.play(mv.col);
            return mv;
        }
        static final class AIMove {
            final int col; final int score; final int depth; final long nodes;
            AIMove(int c, int s, int d, long n) { this.col = c; this.score = s; this.depth = d; this.nodes = n; }
        }
    }
    static final class Board {
        final int rows, cols, connect;
        final int[][] g;
        final int[] heights;
        final Deque<Integer> history = new ArrayDeque<>();
        int currentPlayer = 1;
        final long[][][] zkeys;
        long sideKey;
        long hash = 0L;
        Board(int rows, int cols, int connect) {
            this.rows = rows; this.cols = cols; this.connect = connect;
            this.g = new int[rows][cols];
            this.heights = new int[cols];
            Random rnd = new Random(0xC0FFEE);
            zkeys = new long[rows][cols][2];
            for (int r = 0; r < rows; r++)
                for (int c = 0; c < cols; c++)
                    for (int p = 0; p < 2; p++)
                        zkeys[r][c][p] = rnd.nextLong();
            sideKey = rnd.nextLong();
        }
        void reset() {
            for (int r = 0; r < rows; r++) Arrays.fill(g[r], 0);
            Arrays.fill(heights, 0);
            history.clear();
            currentPlayer = 1;
            hash = 0L;
        }
        boolean play(int col) {
            if (col < 0 || col >= cols) return false;
            int h = heights[col];
            if (h >= rows) return false;
            int row = rows - 1 - h;
            int p = currentPlayer;
            g[row][col] = p;
            heights[col] = h + 1;
            history.push(col);
            hash ^= zkeys[row][col][p - 1];
            hash ^= sideKey;
            currentPlayer = 3 - currentPlayer;
            return true;
        }
        boolean undo() {
            if (history.isEmpty()) return false;
            int col = history.pop();
            int h = heights[col];
            if (h <= 0) return false;
            int row = rows - h;
            int p = g[row][col];
            hash ^= sideKey;
            hash ^= zkeys[row][col][p - 1];
            g[row][col] = 0;
            heights[col] = h - 1;
            currentPlayer = 3 - currentPlayer;
            return true;
        }
        void flipTurn() { currentPlayer = 3 - currentPlayer; }
        boolean isFull() {
            for (int c = 0; c < cols; c++) if (heights[c] < rows) return false;
            return true;
        }
        long getHash() { return hash; }
        int winner() {
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c <= cols - connect; c++) {
                    int p = g[r][c];
                    if (p != 0) {
                        boolean ok = true;
                        for (int k = 1; k < connect; k++) if (g[r][c + k] != p) { ok = false; break; }
                        if (ok) return p;
                    }
                }
            }
            for (int c = 0; c < cols; c++) {
                for (int r = 0; r <= rows - connect; r++) {
                    int p = g[r][c];
                    if (p != 0) {
                        boolean ok = true;
                        for (int k = 1; k < connect; k++) if (g[r + k][c] != p) { ok = false; break; }
                        if (ok) return p;
                    }
                }
            }
            for (int r = 0; r <= rows - connect; r++) {
                for (int c = 0; c <= cols - connect; c++) {
                    int p = g[r][c];
                    if (p != 0) {
                        boolean ok = true;
                        for (int k = 1; k < connect; k++) if (g[r + k][c + k] != p) { ok = false; break; }
                        if (ok) return p;
                    }
                }
            }
            for (int r = connect - 1; r < rows; r++) {
                for (int c = 0; c <= cols - connect; c++) {
                    int p = g[r][c];
                    if (p != 0) {
                        boolean ok = true;
                        for (int k = 1; k < connect; k++) if (g[r - k][c + k] != p) { ok = false; break; }
                        if (ok) return p;
                    }
                }
            }
            return 0;
        }
        boolean isTerminal() { return winner() != 0 || isFull(); }
        List<Integer> legalMoves() {
            List<Integer> colsList = new ArrayList<>();
            for (int c = 0; c < cols; c++) if (heights[c] < rows) colsList.add(c);
            return colsList;
        }
        int evaluate(int forPlayer) {
            int opp = 3 - forPlayer;
            int score = 0;
            int center = cols / 2;
            int centerCount = 0;
            for (int r = 0; r < rows; r++) if (g[r][center] == forPlayer) centerCount++;
            score += centerCount * 4;
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c <= cols - connect; c++) {
                    score += scoreWindow(forPlayer, opp, r, c, 0, 1);
                }
            }
            for (int c = 0; c < cols; c++) {
                for (int r = 0; r <= rows - connect; r++) {
                    score += scoreWindow(forPlayer, opp, r, c, 1, 0);
                }
            }
            for (int r = 0; r <= rows - connect; r++) {
                for (int c = 0; c <= cols - connect; c++) {
                    score += scoreWindow(forPlayer, opp, r, c, 1, 1);
                }
            }
            for (int r = connect - 1; r < rows; r++) {
                for (int c = 0; c <= cols - connect; c++) {
                    score += scoreWindow(forPlayer, opp, r, c, -1, 1);
                }
            }
            return score;
        }
        private int scoreWindow(int me, int opp, int r, int c, int dr, int dc) {
            int meCnt = 0, oppCnt = 0, empty = 0;
            for (int k = 0; k < connect; k++) {
                int v = g[r + k*dr][c + k*dc];
                if (v == me) meCnt++;
                else if (v == opp) oppCnt++;
                else empty++;
            }
            if (oppCnt > 0 && meCnt > 0) return 0;
            if (meCnt == connect) return 200000;
            if (oppCnt == connect) return -200000;
            if (meCnt == connect - 1 && empty == 1) return 2000;
            if (oppCnt == connect - 1 && empty == 1) return -2200;
            if (meCnt == connect - 2 && empty == 2) return 80;
            if (oppCnt == connect - 2 && empty == 2) return -90;
            return 0;
        }
    }
    static final class TranspositionTable {
        static final int EXACT = 0, LOWER = 1, UPPER = 2;

        static final class Entry {
            final long key;
            int depth;
            int value;
            int flag;
            int bestMove;
            Entry(long key, int depth, int value, int flag, int bestMove) {
                this.key = key; this.depth = depth; this.value = value; this.flag = flag; this.bestMove = bestMove;
            }
        }
        private final int cap;
        private final LinkedHashMap<Long, Entry> map;
        TranspositionTable(int capacity) {
            this.cap = capacity;
            this.map = new LinkedHashMap<Long, Entry>(capacity, 0.75f, true) {
                @Override protected boolean removeEldestEntry(Map.Entry<Long, Entry> eldest) {
                    return size() > cap;
                }
            };
        }
        Entry get(long key) { return map.get(key); }
        void put(long key, Entry e) { map.put(key, e); }
        void clear() { map.clear(); }
        int size() { return map.size(); }
    }
    static final class AI {
        private static final int POS_INF = 1_000_000_000;
        private static final int NEG_INF = -POS_INF;

        private static final int TT_CAPACITY = 900_000;
        private final TranspositionTable tt;
        private final int[] moveOrderSeed;
        private final int[][] history;
        private long nodes;
        private boolean timeUp;
        AI(int cols) {
            this.tt = new TranspositionTable(TT_CAPACITY);
            this.moveOrderSeed = centerFirst(cols);
            this.history = new int[3][cols];
        }
        void clearStats() {
            Arrays.fill(history[1], 0);
            Arrays.fill(history[2], 0);
            tt.clear();
        }
        Game.AIMove search(Board board, int maxDepth, int timeSeconds) {
            nodes = 0;
            timeUp = false;
            long deadline = timeSeconds > 0 ? System.nanoTime() + (long)timeSeconds * 1_000_000_000L : Long.MAX_VALUE;
            int bestCol = -1, bestScore = NEG_INF, reached = 0;
            int guess = 0;
            for (int depth = 1; depth <= maxDepth && !timeUp; depth++) {
                int alpha = Math.max(NEG_INF + 1, guess - 200);
                int beta  = Math.min(POS_INF - 1, guess + 200);
                int score;
                while (true) {
                    try {
                        SearchResult res = rootPVS(board, depth, alpha, beta, deadline);
                        score = res.score;
                        if (res.bestCol >= 0) {
                            bestCol = res.bestCol;
                            bestScore = score;
                            reached = depth;
                        }
                    } catch (TimeExceeded te) {
                        timeUp = true;
                        break;
                    }
                    if (score <= alpha) { alpha = Math.max(NEG_INF + 1, alpha - 800); continue; }
                    else if (score >= beta) { beta = Math.min(POS_INF - 1, beta + 800); continue; }
                    break;
                }
                guess = bestScore;
                if (Math.abs(bestScore) > 900_000) break;
                if (System.nanoTime() > deadline) { timeUp = true; break; }
                if (timeSeconds == 0 && depth == maxDepth) break;
            }
            return new Game.AIMove(bestCol, bestScore, reached, nodes);
        }
        private static final class SearchResult {
            final int bestCol; final int score;
            SearchResult(int c, int s) { this.bestCol = c; this.score = s; }
        }
        private SearchResult rootPVS(Board b, int depth, int alpha, int beta, long deadline) {
            List<Integer> moves = orderedMoves(b, -1);
            int bestCol = -1;
            int bestScore = NEG_INF;
            boolean first = true;
            for (int col : moves) {
                if (System.nanoTime() > deadline) throw new TimeExceeded();
                if (!b.play(col)) continue;
                int sc;
                if (first) {
                    sc = -pvs(b, depth - 1, -beta, -alpha, b.currentPlayer == 1 ? 2 : 1, deadline, true, 0);
                    first = false;
                } else {
                    sc = -pvs(b, depth - 1, -alpha - 1, -alpha, b.currentPlayer == 1 ? 2 : 1, deadline, false, 0);
                    if (sc > alpha && sc < beta) {
                        sc = -pvs(b, depth - 1, -beta, -alpha, b.currentPlayer == 1 ? 2 : 1, deadline, true, 0);
                    }
                }
                b.undo();
                if (sc > bestScore) { bestScore = sc; bestCol = col; }
                if (sc > alpha) alpha = sc;
                if (alpha >= beta) break;
            }
            return new SearchResult(bestCol, bestScore);
        }
        private int pvs(Board b, int depth, int alpha, int beta, int rootPlayer, long deadline, boolean pvNode, int moveCount) {
            if (System.nanoTime() > deadline) throw new TimeExceeded();
            nodes++;
            int winner = b.winner();
            if (winner != 0) {
                if (winner == rootPlayer) return 1_000_000 - (1000 - depth);
                else return -1_000_000 + (1000 - depth);
            }
            if (depth == 0 || b.isFull()) {
                return b.evaluate(rootPlayer) - b.evaluate(3 - rootPlayer);
            }
            TranspositionTable.Entry e = tt.get(b.getHash());
            if (e != null && e.depth >= depth) {
                if (e.flag == TranspositionTable.EXACT) return e.value;
                else if (e.flag == TranspositionTable.LOWER && e.value > alpha) alpha = e.value;
                else if (e.flag == TranspositionTable.UPPER && e.value < beta) beta = e.value;
                if (alpha >= beta) return e.value;
            }
            int bestVal = NEG_INF;
            int bestMove = -1;
            boolean first = true;
            List<Integer> moves = orderedMoves(b, e != null ? e.bestMove : -1);
            int idx = 0;
            for (int col : moves) {
                idx++;
                int reduction = 0;
                boolean isImmediateWin = false;
                int r = b.rows - 1 - b.heights[col];
                if (r >= 0) {
                    b.g[r][col] = b.currentPlayer;
                    isImmediateWin = winsAt(b, r, col);
                    b.g[r][col] = 0;
                }
                if (!pvNode && depth >= 3 && idx > 3 && !isImmediateWin) {
                    reduction = 1;
                }
                if (!b.play(col)) continue;
                int val;
                if (first) {
                    val = -pvs(b, depth - 1, -beta, -alpha, rootPlayer, deadline, pvNode, idx);
                    first = false;
                } else {
                    val = -pvs(b, depth - 1 - reduction, -alpha - 1, -alpha, rootPlayer, deadline, false, idx);
                    if (val > alpha && val < beta) {
                        val = -pvs(b, depth - 1, -beta, -alpha, rootPlayer, deadline, true, idx);
                    }
                }
                b.undo();
                if (val > bestVal) { bestVal = val; bestMove = col; }
                if (val > alpha) alpha = val;
                if (alpha >= beta) {
                    history[b.currentPlayer][col] += depth * depth;
                    break;
                }
            }
            int flag;
            if (bestVal <= alpha) flag = TranspositionTable.UPPER;
            else if (bestVal >= beta) flag = TranspositionTable.LOWER;
            else flag = TranspositionTable.EXACT;
            tt.put(b.getHash(), new TranspositionTable.Entry(b.getHash(), depth, bestVal, flag, bestMove));
            return bestVal;
        }
        private List<Integer> orderedMoves(Board b, int ttBest) {
            List<Integer> legal = new ArrayList<>(b.cols);
            for (int c : moveOrderSeed) if (b.heights[c] < b.rows) legal.add(c);
            if (ttBest >= 0 && legal.remove((Integer)ttBest)) legal.add(0, ttBest);
            for (int i = 0; i < legal.size(); i++) {
                int c = legal.get(i);
                int r = b.rows - 1 - b.heights[c];
                if (r >= 0) {
                    b.g[r][c] = b.currentPlayer;
                    boolean win = (winsAt(b, r, c));
                    b.g[r][c] = 0;
                    if (win) { legal.remove(i); legal.add(0, c); }
                }
            }
            legal.sort((c1, c2) -> {
                int h1 = history[b.currentPlayer][c1];
                int h2 = history[b.currentPlayer][c2];
                if (h1 != h2) return Integer.compare(h2, h1);
                int center = b.cols / 2;
                int d1 = Math.abs(center - c1);
                int d2 = Math.abs(center - c2);
                return Integer.compare(d1, d2);
            });
            return legal;
        }
        private boolean winsAt(Board b, int r, int c) {
            int p = b.currentPlayer;
            int need = b.connect;
            int count = 1;
            for (int dc = c - 1; dc >= 0 && b.g[r][dc] == p; dc--) count++;
            for (int dc = c + 1; dc < b.cols && b.g[r][dc] == p; dc++) count++;
            if (count >= need) return true;
            count = 1;
            for (int dr = r + 1; dr < b.rows && b.g[dr][c] == p; dr++) count++;
            if (count >= need) return true;
            count = 1;
            for (int dr = r - 1, dc = c + 1; dr >= 0 && dc < b.cols && b.g[dr][dc] == p; dr--, dc++) count++;
            for (int dr = r + 1, dc = c - 1; dr < b.rows && dc >= 0 && b.g[dr][dc] == p; dr++, dc--) count++;
            if (count >= need) return true;
            count = 1;
            for (int dr = r - 1, dc = c - 1; dr >= 0 && dc >= 0 && b.g[dr][dc] == p; dr--, dc--) count++;
            for (int dr = r + 1, dc = c + 1; dr < b.rows && dc < b.cols && b.g[dr][dc] == p; dr++, dc++) count++;
            return count >= need;
        }
        private int[] centerFirst(int cols) {
            int[] order = new int[cols];
            int center = cols / 2;
            int i = 0;
            order[i++] = center;
            for (int off = 1; off <= center; off++) {
                int l = center - off;
                int r = center + off;
                if (r < cols) order[i++] = r;
                if (l >= 0)  order[i++] = l;
            }
            for (; i < cols; i++) order[i] = i;
            return order;
        }
        static final class TimeExceeded extends RuntimeException {}
    }
    static final class Renderer {
        private static final String RESET = "\u001b[0m";
        private static final String BRIGHT_YELLOW = "\u001b[93m";
        private static final String BRIGHT_CYAN = "\u001b[96m";
        private static final String BRIGHT_WHITE = "\u001b[97m";
        static void printBanner(boolean ansi) {
            if (ansi) clearScreenIfAnsi(true);
            System.out.println("+-------------------------------------------+");
            System.out.println("|            Connect Four by amir           |");
            System.out.println("+-------------------------------------------+");
        }
        static void printHelp(int cols) {
            System.out.println("Commands:");
            System.out.println("  1.." + cols + "   - drop a piece into that column");
            System.out.println("  depth N    - set fixed AI search depth (1..22)");
            System.out.println("  time S     - set time per move in seconds (0 = use fixed depth)");
            System.out.println("  u / undo   - undo your last move (and AI's response if present)");
            System.out.println("  auto [n]   - AI vs AI for n plies (default 1)");
            System.out.println("  new        - restart the game");
            System.out.println("  help       - show this help");
            System.out.println("Tip: Use --ansi false to disable colors, --anim false to disable drop animation.");
            System.out.println();
        }
        static void clearScreenIfAnsi(boolean ansi) {
            if (!ansi) return;
            System.out.print("\u001b[H\u001b[2J");
            System.out.flush();
        }
        static void render(Board b, int overlayRow, int overlayCol, int overlayPlayer, boolean ansi) {
            String empty = ansi ? BRIGHT_WHITE + "· " + RESET : ". ";
            String human = ansi ? BRIGHT_YELLOW + "X▲" + RESET : "X^";
            String ai    = ansi ? BRIGHT_CYAN   + "O●" + RESET : "Oo";
            System.out.println();
            for (int r = 0; r < b.rows; r++) {
                System.out.print("|");
                for (int c = 0; c < b.cols; c++) {
                    String token;
                    if (r == overlayRow && c == overlayCol && overlayPlayer != 0) {
                        token = overlayPlayer == 1 ? human : ai;
                    } else {
                        int v = b.g[r][c];
                        if (v == 0) token = empty;
                        else token = (v == 1 ? human : ai);
                    }
                    System.out.print(" " + token + " ");
                }
                System.out.println("|");
            }
            System.out.print(" ");
            for (int c = 1; c <= b.cols; c++) {
                System.out.print(" " + c + "  ");
            }
            System.out.println();
            System.out.println("Turn: " + (b.currentPlayer == 1 ? "Human (X▲)" : "AI (O●)"));
            System.out.println();
        }
    }
    static final class CliArgs {
        final int rows, cols, depth, timeSeconds;
        final boolean aiFirst, ansi, anim;
        final int animDelayMs;
        CliArgs(int rows, int cols, int depth, int timeSeconds, boolean aiFirst, boolean ansi, boolean anim, int animDelayMs) {
            this.rows = rows; this.cols = cols; this.depth = depth; this.timeSeconds = timeSeconds;
            this.aiFirst = aiFirst; this.ansi = ansi; this.anim = anim; this.animDelayMs = animDelayMs;
        }
        static CliArgs parse(String[] args) {
            int rows = 6, cols = 7, depth = 16, timeSeconds = 12, animDelay = 40;
            boolean aiFirst = true, ansi = true, anim = true;
            for (int i = 0; i < args.length; i++) {
                switch (args[i]) {
                    case "--rows": if (i + 1 < args.length) rows = clampInt(args[++i], 4, 9, rows); break;
                    case "--cols": if (i + 1 < args.length) cols = clampInt(args[++i], 4, 10, cols); break;
                    case "--depth": if (i + 1 < args.length) depth = clampInt(args[++i], 1, 22, depth); break;
                    case "--time": if (i + 1 < args.length) timeSeconds = clampInt(args[++i], 0, 60, timeSeconds); break;
                    case "--ai-first": if (i + 1 < args.length) aiFirst = parseBool(args[++i], aiFirst); break;
                    case "--ansi": if (i + 1 < args.length) ansi = parseBool(args[++i], ansi); break;
                    case "--anim": if (i + 1 < args.length) anim = parseBool(args[++i], anim); break;
                    case "--anim-delay": if (i + 1 < args.length) animDelay = clampInt(args[++i], 0, 500, animDelay); break;
                }
            }
            return new CliArgs(rows, cols, depth, timeSeconds, aiFirst, ansi, anim, animDelay);
        }
        private static int clampInt(String s, int min, int max, int def) {
            try { int v = Integer.parseInt(s); return (v < min || v > max) ? def : v; }
            catch (NumberFormatException e) { return def; }
        }
        private static boolean parseBool(String s, boolean def) {
            String v = s.toLowerCase(Locale.ROOT);
            if (v.equals("true") || v.equals("t") || v.equals("1") || v.equals("yes") || v.equals("y")) return true;
            if (v.equals("false") || v.equals("f") || v.equals("0") || v.equals("no") || v.equals("n")) return false;
            return def;
        }
    }
}