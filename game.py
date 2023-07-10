#!env/bin/python
import cfrais, time
from dataclasses import dataclass

RATE = 44100
DEVICE = 1

def print_synergization(synergized):
    print("                 SYNERGY COMPLETE")
    print()
    print("  Synergized %s, %s, and %s:" % tuple(synergized))
    print()
    print("     ***************************************")
    print("     * I'm not sure if any of this matters *")
    print("     *             to me anymore.          *")
    print("     ***************************************")
    print()

class game:
    def __init__(self):
        self.state = ["unsynergized", []]
        self.start()

    def start(self):
        print("    This is the ARTIFICIAL BUSINESS SYNERGY SYSTEM.")
        print()
        print("        LUXURY MANAGEMENT CORPORATION 2023")
        print()
        print("    Tell the computer to consider powerful business")
        print("    concepts by saying: COMPUTER, CONSIDER STOCKS")
        print()
        print("    You can also simply say: COMPUTER, STOCKS")
        print()
        print("    Once you have input three business ideas, tell the")
        print("    computer to connect them into a BUSINESS SYNERGY")
        print("    by saying: COMPUTER, SYNERGIZE.")
        print()
        print("    You need 3 more concepts to synergize.")
        print()

    def do(self, it):
        if isinstance(it, ConsiderBusinessIdea):
            self.do_considerbusinessidea(it.idea)
        elif isinstance(it, Synergize):
            self.do_synergize()

    def do_considerbusinessidea(self, it):
        if self.state[0] == "unsynergized" and len(self.state[1]) < 3:
            print()
            print("Considering %s..." % it)
            print()
            self.state[1].append(it)
            self.print_situation()
        elif self.state[0] == "unsynergized":
            print()
            print("You can't synergize more than three ideas.")
            print()
            print("That would be Forbidden Business.")
            print()
        else:
            print("Synergy is already complete!")
            print()
            print("No more business ideas can be known.")
            print()
            print("   \"After synergy, no more business ideas can be known.\"")
            print("        -- William Buffett, probably")

    def do_synergize(self):
        if self.state[0] == "unsynergized":
            if len(self.state[1]) < 3:
                print()
                print("Not enough business ideas.")
                print()
                print("You need exactly three business ideas to synergize.")
                print()
            else:
                print()
                for j in range(24):
                    print("       --------**** SYNERGIZING! ****-------")
                    time.sleep(0.06)
                    print()
                    time.sleep(0.1)
                print()
                self.state[0] = "synergized"
                print()
                print()
                print()
                print_synergization(self.state[1])
        else:
            print()
            print("Synergy is already done.")

    def print_situation(self):
        if self.state[0] == "unsynergized":
            print()
            print("Now synergizing the following business concepts:")
            print()
            for concept in self.state[1]:
                print()
                print(" " * 20 + concept)
            print()

            if len(self.state[1]) < 3:
                amount = 3 - len(self.state[1])
                print("    Need %d more concept%s to synergize." %
                      (amount, "" if amount == 1 else "s"))
                     
            else:
                print("    Three concepts known. Ready to synergize.")
                print()
                print("    To synergize, say COMPUTER, SYNERGIZE.")
            
@dataclass
class ConsiderBusinessIdea:
    idea: str

@dataclass
class Synergize:
    pass

class transformer:
    def parse(self, what):
        if what[0] == what[0].upper():
            return what[0]
        what = [what[0], *[self.parse(it) for it in what[1:]]]
        fn = getattr(self, "parse_" + what[0], None)
        if fn is None:
            raise Exception("no method parse_" + what[0])
        else:
            return fn(what)

    def parse_maybe_please(self, what):
        return "please?"

    def parse_business(self, what):
        return what[1]

    def parse_short(self, what):
        return what[1]

    def parse_computer_consider_business_idea(self, what):
        return ConsiderBusinessIdea(what[4])

    def parse_business_idea(self, what):
        return what[1]

    def parse_maybe_verb(self, what):
        return what

    def parse_synergize(self, what):
        return Synergize()

class statement_processor(cfrais.chat.ThatStatementProcessor):
    def __init__(self, *args):
        super().__init__(*args)
        self.transformer = transformer()
        self.game = game()
    def do(self, what):
        #print("input:", what)
        self.game.do(self.transformer.parse(what))

def run_chat(larkdir):
    for i in range(4):
        try:
            cfrais.stream.stream(
                'models/model.tflite',
                'models/listen.scorer',
                cfrais.parser.parser(larkdir),
                statement_processor,
                input_rate=RATE,
                device=DEVICE,
            ).start()
            print("got here?")
            return
                
        except OSError:
            import traceback
            traceback.print_exc()
            print("attempt %d: waiting 20 seconds and trying again" % i)
            time.sleep(20.0)
