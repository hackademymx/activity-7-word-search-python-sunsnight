
import wordSearch

def test_one():
    wordSearch.wordSearch('ALLESSAYIOPEBUTNRACANHHEHREFOXIAAERUIFNRPRGELTHXSHWTUOHSTCURLITE', ['thin', 'oil', 'tube', 'fox', 'thought', 'curl', 'air', 'essay', 'shout', 'era']) == True

def test_two():
    assert wordSearch.wordSearch('DELDNUBPETENHARALOSSOUNTPCHIEFDRUROHSOTZOAWENINLCLPOKERFORBIDMTC', ['crisis', 'kit', 'pat', 'chief', 'show', 'poker', 'forbid', 'couple', 'donor', 'bundle']) == False

def test_three():
    wordSearch.wordSearch('LOBMYSALORDOTRECENTENSIOXAUEDNDYLHSAMTLFVEINNLBLSECOACERTYMRBFEH', ['nuance', 'record', 'helmet', 'rally', 'parade', 'tension', 'symbol', 'separate', 'vein', 'ash']) == False

def test_four():
    wordSearch.wordSearch('PEANUTIHATEFOUSTLAGBRYUGAGAOANSNCVSTXENEEISTSDERNUELHOCTTAMEPROS', ['gate', 'bee', 'bottle', 'deny', 'census', 'peanut', 'message', 'palace', 'next', 'strength']) == True

def test_five():
    wordSearch.wordSearch('CAFZEROTEOALGWNNGSNEAECIIZPCDGFSTTDIEBFUFASCEINOIELNURVCRHTXGMCE', ['ice', 'cousin', 'resident', 'conceive', 'drift', 'heat', 'zero', 'flag', 'run', 'pierce'])  == False

def test_six():
    wordSearch.wordSearch('KARALLOCGNTEBMAIBHEOCPFMRUNEOFUMAWGKDURAVDRECAZSEMJALOTSOXVACUNU', ['mass', 'cap', 'brave', 'knee', 'collar', 'alarm', 'vacuum', 'leg', 'fur', 'lot']) == True

def test_seven():
    wordSearch.wordSearch('NYBNETADOORTNAOESAYHOPDLITRSEOWIRSHEWHRVPOGWOSNEFAMILIARTENESBHT', ['ant', 'age', 'familiar', 'net', 'root', 'say', 'prison', 'bishop', 'deliver', 'slow']) == True

def test_eight():
    wordSearch.wordSearch('HOAIKPMKWDBNSEECIEESAHMAZFDTCRBBCIRIAUEDANONPSRETEECSHOECRTTTSIF', ['debate', 'ask', 'member', 'rush', 'obscure', 'instinct', 'feed', 'fist', 'all', 'catch']) == False

def test_nine():
    wordSearch.wordSearch('EBEGLAEROZPOSTVLKYEEONEOCUTETEISIBUYRCHTRMYGSBCNTCERIDAPRDIKOMAN', ['buy', 'lost', 'real', 'breeze', 'direct', 'man', 'post', 'trick', 'degree', 'achieve']) == True

def test_ten():
    wordSearch.wordSearch('MITSFOCAERCULTURMDHYKIRTGLANCELMYPRODUCEODICSVLGLETSOOADPRYGHMNI', ['produce', 'charity', 'employ', 'art', 'gem', 'raid', 'glance', 'hole', 'moon', 'ear']) == False